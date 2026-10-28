# The recorded consent notice

Owner: WS1 (#7). Every call plays this before anyone answers. It is the consent step in
[ethics.md](ethics.md), so a missing or broken file is a launch blocker, not a polish item.

## What to record

The script is in [copy.md](copy.md#consent-notice-script-for-mahak-7): Hindi first, then
English, in a normal speaking voice (not an IVR voice: it must not sound like one of the
arms). The wording must say: it is a game, you may talk to an AI, the call is recorded for
research, do not share personal details, stay on the line to agree or hang up now.

**Length.** Callers cannot skip it and long notices make people hang up before the game
starts. #7 asks for about 20 s; the script as written is two blocks of roughly 12 to 15
seconds, so about 25 to 30 s together. Time your take (`ffprobe`, below). If it runs long,
trim words rather than speaking faster, and agree the cut with Abhinav, since the text
lives in copy.md and the site repeats it.

## Record and export

1. Record in a quiet room on a phone, one take per language or both in one take. No music.
2. Trim silence at the start and end (aim for under half a second).
3. Export mono, 16 kHz MP3 (Plivo recommends 8 or 16 kHz mono, https, at most 10 MB):

   ```bash
   ffmpeg -i raw.m4a -ac 1 -ar 16000 -b:a 48k -af loudnorm consent.mp3
   ffprobe -v error -show_entries format=duration -of default=nw=1 consent.mp3
   ```

   A 30 s notice at this setting is about 180 KB.
4. Play it **on a phone speaker and through the phone line** (the first test call), not
   only on laptop headphones: that is how callers hear it.

## Host it

Plivo fetches the file by URL, so it needs a stable **https** address.

- **Default:** put it at `web/public/consent.mp3` and set
  `CONSENT_AUDIO_URL=https://<site>/consent.mp3`. This works once the site is deployed
  (WS3-06, #26). `.gitignore` blocks `*.mp3` (call recordings) but allows exactly this
  path, since the notice is not call data.
- **Before the site is live:** any https static host works for a test. Do not point
  production at a personal or temporary link: if it disappears, every call loses its
  consent notice.

Set the variable as a host secret (see [deploy.md](deploy.md)). Unset, callers hear the
text-to-speech fallback instead.

## Check it

```bash
cd backend && uv run pk check-consent
```

It fetches the URL the way the vendor does and fails on: not https, not 200, not an audio
content type, under 4 KB or over 10 MB, or bytes that are not MP3/WAV. It cannot hear the
notice, so it does not replace listening to it. `pk check-consent --allow-tts` accepts an
unset URL (rehearsals only).

Then make a real call and check, in this order:

1. The notice plays **fully** before the dial starts, in both languages.
2. Hanging up during it ends the call with no arm contacted (the Call row stays `routed`
   and never reaches `processed`).
3. The call recording starts **after** the arm answers, so the notice is not in it.

## Things not known

- **What Plivo does when the file cannot be fetched.** Its `<Play>` docs do not say, and
  the XML has no "else" branch. That is why `pk check-consent` exists: run it after every
  change to the URL or the host, and again on launch day (#10).
- **The text-to-speech fallback is weak.** Plivo's `<Speak>` has no Hindi or Indian-English
  voice (its language list stops at en-US/GB/AU and European languages), so an English voice
  reads the Hindi half. It says the same words, which is enough for a rehearsal, not for
  launch.
