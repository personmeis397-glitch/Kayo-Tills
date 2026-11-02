# Contributing

Thanks for helping improve Kayo Tills!

1. Fork the repo and create a branch: `git checkout -b feature/my-change`
2. Make your change. The piano lives in `app/src/main/assets/www/index.html`;
   the Android shell is in `app/src/main/java/com/kayotills/app/`.
3. Run `./gradlew testDebugUnitTest lint assembleDebug` and make sure it passes.
4. Test on a real device or emulator in landscape, in both light and dark mode.
5. Open a pull request describing what changed and why.

Guidelines:
- Keep the app offline and permission-free. Changes that add network access or
  permissions need a strong reason and a PRIVACY.md update.
- Follow `.editorconfig` and Kotlin official code style.
- Add a line to `CHANGELOG.md` under "Unreleased".
