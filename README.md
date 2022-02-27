# trollSpeak
this is a little python tool to help with homestuck troll typing quirks that also copies the output to your clipboard.

# usage
simply enter the name of a troll (that's currently supported) at the prompt. from there type in whatever text you wish and it will be converted following that selected troll's quirk. to return to the select prompt simply enter "quit()", and do so again at the prompt to quit entirely. 

note that you will need to provide it with sufficient input, there are certain things it just won't do. for example the vriska function does not auto-capitalize your sentences, nor does it work with every single 8 pun (yet). you will have to do other things as well like draaaaaaaag out vowels or use the right number of colons in your emoticons. the terezi function will not convert your emoticons. there is not currently nor will there ever be a karkat function either, because your keyboard is conventiently already equipped with one. it's called your caps lock key. 

eventually once i add the rest of the beta trolls i'll probably add the alpha trolls. i haven't checked out friendsim or hiveswap so i probably won't add those, nor will i probably add anything added by homestuck^2. if i don't add your favorite troll then hopefully the code is obvious enough you can simply add them in yourself. you can also do this with your fantrolls if you wish. go nuts. fantrolls are dope and if i had any i'd add their quirks myself.

# requirements
this uses python 3 and a library called "clipboard" which you can easily install via pip (https://pypi.org/project/clipboard/ is the link).

# changelog
v0.3 - initial version, contains quirks for kanaya, terezi, and vriska.

v0.6 - added gamzee, eridan, and sollux. rewrote clipboard bits so as to make use of a less inconvenient library. 

v0.6.1 - fixed a bug in eridan's quirk.
