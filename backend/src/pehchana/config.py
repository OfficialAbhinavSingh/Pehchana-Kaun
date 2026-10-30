"""Runtime settings, loaded from environment variables (see ../../.env.example)."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

from dotenv import dotenv_values
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

REPO_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(REPO_ROOT / ".env", ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    env: str = "dev"
    # Public base URL of this backend. Plivo and Bolna call back into it, so in dev
    # it is usually an ngrok / cloudflared tunnel URL.
    public_base_url: str = "http://localhost:8000"
    database_url: str = "sqlite:///./pehchana.db"
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:3000"])

    # Salt for hashing caller phone numbers. We never store raw numbers.
    caller_hash_salt: str = "change-me"
    # Shared secret for /admin endpoints (shift toggles, reprocessing).
    admin_token: str = "change-me"

    arms_file: Path = REPO_ROOT / "bolna" / "arms.yaml"

    # Bolna
    bolna_api_key: str = ""
    bolna_base_url: str = "https://api.bolna.ai"
    # Shared secret Bolna sends back to us in a header on custom-function calls and
    # webhooks (configured per agent), since Bolna does not sign requests.
    bolna_shared_secret: str = "change-me"
    bolna_webhook_ips: list[str] = Field(
        default_factory=lambda: ["13.203.39.153", "13.126.9.249", "13.202.133.53"]
    )
    enforce_bolna_ip_allowlist: bool = False

    # Which telephony vendor handles the public number (see telephony/registry.py).
    telephony_provider: str = "plivo"

    # Plivo
    plivo_auth_id: str = ""
    plivo_auth_token: str = ""
    plivo_number: str = ""
    consent_audio_url: str = ""
    # Which stereo channel of the Plivo session recording carries the caller (A-leg).
    # Verify on Day 1 with a test call and flip if needed.
    caller_channel: int = 0
    # Hosts a recording URL may point at (exact match, https only). Recording URLs come
    # from webhooks, so anything else is refused before it is stored. Plivo serves
    # recordings from media.plivo.com; confirm on the first real call and add any other
    # host it uses. Other telephony vendors need their own host listed here.
    recording_host_allowlist: list[str] = Field(
        default_factory=lambda: ["media.plivo.com", "api.bolna.ai"]
    )
    # Largest recording we will download. 10 min of stereo 8 kHz 16-bit WAV is ~19 MB.
    recording_max_bytes: int = 50_000_000

    # Deepgram (post-call, timestamped transcription of the recording)
    deepgram_api_key: str = ""
    deepgram_model: str = "nova-3"
    deepgram_language: str = "multi"

    # Claude (post-call giveaway tagging; free fallbacks: Groq or Gemini)
    anthropic_api_key: str = ""
    tagger_model: str = "claude-opus-5"
    groq_api_key: str = ""
    gemini_api_key: str = ""

    # Leaderboard
    reveal_vendors: bool = False
    include_demo_data: bool = False
    min_calls_for_ranking: int = 5
    # Seconds one computed leaderboard is served before it is rebuilt (0 = no cache).
    leaderboard_cache_s: float = 30.0

    # Browser game (POST /webcall/session). Every session is a paid Bolna call, so cap
    # sessions per client IP and in total.
    webcall_per_ip: int = 3
    webcall_per_ip_window_s: float = 600.0
    webcall_per_hour: int = 120

    @field_validator("database_url")
    @classmethod
    def _postgres_driver(cls, url: str) -> str:
        """Hosts hand out ``postgres://`` or ``postgresql://`` URLs. SQLAlchemy would read
        the first as an unknown dialect and the second as psycopg2, which we do not ship."""
        for prefix in ("postgres://", "postgresql://"):
            if url.startswith(prefix):
                return "postgresql+psycopg://" + url[len(prefix) :]
        return url

    def production_problems(self) -> list[str]:
        """Reasons this configuration must not serve real callers (empty when fine).

        The defaults are for local dev; deployed with them, ``/admin`` would accept
        ``change-me`` and caller hashes could be reversed from a known salt.
        """
        problems = []
        for name in ("admin_token", "caller_hash_salt", "bolna_shared_secret"):
            value = getattr(self, name)
            if value in ("", "change-me"):
                problems.append(f"{name.upper()} is unset or still the dev default")
            elif len(value) < 16 and name != "bolna_shared_secret":
                problems.append(f"{name.upper()} is shorter than 16 characters")
        if not self.plivo_auth_token:
            problems.append("PLIVO_AUTH_TOKEN is unset, so every webhook would be refused")
        if not self.public_base_url.startswith("https://"):
            problems.append("PUBLIC_BASE_URL must be https:// (vendors sign the public URL)")
        if self.database_url.startswith("sqlite"):
            problems.append("DATABASE_URL points at SQLite; production uses Postgres")
        if self.include_demo_data:
            problems.append("INCLUDE_DEMO_DATA=true would put fake calls in the public stats")
        return problems

    def production_warnings(self) -> list[str]:
        """Things worth fixing that do not stop a launch."""
        warnings = []
        if all("localhost" in origin or "127.0.0.1" in origin for origin in self.cors_origins):
            warnings.append("CORS_ORIGINS only allows localhost: the deployed site cannot call us")
        if not self.consent_audio_url:
            warnings.append("CONSENT_AUDIO_URL is unset: callers hear the text-to-speech notice")
        if not self.bolna_api_key:
            warnings.append("BOLNA_API_KEY is unset: browser games cannot start")
        if not self.deepgram_api_key:
            warnings.append("DEEPGRAM_API_KEY is unset: calls cannot be transcribed or scored")
        return warnings


@lru_cache
def get_settings() -> Settings:
    return Settings()


def arm_env() -> dict[str, str]:
    """Env vars named in arms.yaml. Settings reads .env itself, so merge it in here."""
    values = {k: v for k, v in dotenv_values(REPO_ROOT / ".env").items() if v is not None}
    return {**values, **os.environ}
