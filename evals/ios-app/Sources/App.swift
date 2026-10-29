import FirebaseAnalytics
import GoogleMobileAds
func login(user: User) {
    NSLog("login email=%@ phone=%@", user.email, user.phone)
    Analytics.logEvent("login", parameters: nil)
}
let isOn = true // marketing consent toggle default
