import Ruleset
import AlertLogger
def checkMessage(author,message):
    if Ruleset.isBadLink(message):
        AlertLogger.logAlert(str(author),"non-clip link posted in chat",str(message))
        return 1
    if Ruleset.notEnglish(message):
        AlertLogger.logAlert(str(author),"language detected as not english by cld3 with over 90% probability",str(message))
        return 1
