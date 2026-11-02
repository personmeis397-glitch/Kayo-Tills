package com.kayotills.app

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class AppConfigTest {
    @Test
    fun startUrlIsInternal() {
        assertTrue(AppConfig.isInternalUrl(AppConfig.START_URL))
    }

    @Test
    fun externalUrlsAreBlocked() {
        assertFalse(AppConfig.isInternalUrl("https://example.com/assets/www/index.html"))
        assertFalse(AppConfig.isInternalUrl("http://${AppConfig.HOST}/assets/www/index.html"))
        assertFalse(AppConfig.isInternalUrl("https://${AppConfig.HOST}.evil.com/assets/"))
        assertFalse(AppConfig.isInternalUrl("file:///data/data/com.kayotills.app/secret"))
    }
}
