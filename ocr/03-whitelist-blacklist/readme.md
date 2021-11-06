## whitelist
1. Add this to config
options += "-c tessedit_char_whitelist="0123456789$.-"
#### include these characters and only these characters
#### P.S - notice no space

## blacklist
1. same logic as in whitelist
options += "-c tessedit_char_blacklist="*#"


## we can combine both of those as well