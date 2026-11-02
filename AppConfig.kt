package com.kayotills.app

/** Central place for the URLs the in-app WebView is allowed to use. */
object AppConfig {
    /** Virtual HTTPS origin served from bundled assets (gives the app a stable origin for localStorage). */
    const val HOST = "appassets.androidplatform.net"
    const val START_URL = "https://$HOST/assets/www/index.html"
    const val USER_AGENT_SUFFIX = " KayoTills/1.0"

    /** True only for pages that belong to the bundled app. */
    fun isInternalUrl(url: String): Boolean = url.startsWith("https://$HOST/assets/")
}
