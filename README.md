# Kayo Tills

[![Android CI](../../actions/workflows/android.yml/badge.svg)](../../actions/workflows/android.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Min SDK 26](https://img.shields.io/badge/minSdk-26-green)

A pocket grand piano for Android. All 88 keys on one landscape screen, four piano
voices, sustain pedal, reverb, and a live frequency (Hz) chart. Fully offline, no
ads, no accounts, **no permissions**.

## Features

- 88 keys (A0 to C8) in three stacked layers, with colour-lit keys
- Four voices: Steinway & Sons, Fazioli, Blüthner, C. Bechstein
- Velocity-sensitive touch (press lower on a key to play louder) and glide across keys
- Sustain pedal, volume and reverb controls
- Note names, note names + Hz, or no labels
- Frequency chart for every key (tap a row to hear it)
- Remembers your settings, follows system light/dark mode
- Immersive landscape layout, screen stays awake while you play

## How it works

The app is a small native Kotlin shell around a self-contained web app.
The piano itself (`app/src/main/assets/www/index.html`) is plain HTML/CSS/JS using
the Web Audio API. `MainActivity` serves it from bundled assets through
`WebViewAssetLoader`, blocks all outside navigation, and enforces a strict
Content-Security-Policy. Nothing is loaded from the network.

```
kayo-tills/
├── app/
│   ├── build.gradle.kts
│   └── src/
│       ├── main/
│       │   ├── assets/www/        # the piano (HTML/CSS/JS) + fonts/
│       │   ├── java/com/kayotills/app/
│       │   │   ├── MainActivity.kt
│       │   │   └── AppConfig.kt
│       │   └── res/               # icons, themes, strings
│       └── test/                  # unit tests
├── fastlane/metadata/android/     # store listing text
├── scripts/fetch-fonts.py         # optional: bundle fonts for offline use
├── .github/                       # CI, issue and PR templates, Dependabot
└── gradle/libs.versions.toml      # dependency versions
```

## Build

Requirements: JDK 17 and the Android SDK (or just Android Studio).

**Android Studio:** open the folder, let Gradle sync, press Run.

**Command line:**

```bash
# one-time: generate the Gradle wrapper (needs Gradle 8.9+ installed)
gradle wrapper --gradle-version 8.9

./gradlew testDebugUnitTest assembleDebug
# APK: app/build/outputs/apk/debug/kayo-tills-debug.apk
```

Commit the generated `gradlew`, `gradlew.bat` and `gradle/wrapper/` files so
everyone gets the same Gradle version.

## Optional: bundle the original fonts

The design uses Instrument Sans, Instrument Serif and DM Mono. Until you run the
script below, the app falls back to system fonts (it still looks right, just not
identical). Run once with internet access, then commit the result:

```bash
python3 scripts/fetch-fonts.py
```

## Signed releases (GitHub Actions)

Pushing a tag like `v1.0.0` builds and publishes a GitHub Release.

1. Create a keystore (keep it safe, you need the same one for every update):
   ```bash
   keytool -genkeypair -v -keystore kayo-tills.jks -alias kayo \
     -keyalg RSA -keysize 2048 -validity 10000
   base64 -w0 kayo-tills.jks > kayo-tills.jks.b64   # macOS: base64 -i kayo-tills.jks
   ```
2. In **Settings → Secrets and variables → Actions** add:
   `KEYSTORE_BASE64` (contents of the `.b64` file), `KEYSTORE_PASSWORD`,
   `KEY_ALIAS`, `KEY_PASSWORD`.
3. Bump `versionCode` / `versionName` in `app/build.gradle.kts`, update
   `CHANGELOG.md`, then:
   ```bash
   git tag v1.0.0 && git push origin v1.0.0
   ```

Without the secrets, the release job attaches a debug-signed APK instead, which is
fine for testing but not for the Play Store.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Security issues: [SECURITY.md](SECURITY.md).
Privacy: [PRIVACY.md](PRIVACY.md).

## License

[MIT](LICENSE)
