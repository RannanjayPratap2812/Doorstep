#!/usr/bin/env bash
# Run after `npx cap add android`: adds ringtones and alarm permissions.
set -e
mkdir -p android/app/src/main/res/raw
cp ringtones/*.wav android/app/src/main/res/raw/
M=android/app/src/main/AndroidManifest.xml
grep -q SCHEDULE_EXACT_ALARM $M || sed -i 's#<application#<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM"/>\n    <uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>\n    <application#' $M
