app_name = "chinese_utils"
app_title = "Chinese Utils"
app_publisher = "Your Name"
app_description = "Chinese number conversion utilities for ERPNext"
app_email = "your.email@example.com"
app_license = "MIT"

# This is the important part - registering the function for Jinja
jenv = {
    "methods": [
        "chinese_utils.custom_functions.money_in_chinese"
    ]
}

# Add this new section
jinja = {
    "methods": [
        "chinese_utils.custom_functions.money_in_chinese"
    ]
}
