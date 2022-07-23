# Emoji.js

Demo 
> https://anonymousxc.github.io/emoji.js/



## Documentation
---

```javascript
new EmojiPicker({
    trigger: [
        {
            selector: '.btn1',
            insertInto: ['.txt0', '.txt1']
        },
        {
            selector: '#btn2',
            insertInto: '.txt1'
        }
    ],
    closeButton: true,
    dragButton: true,
    width: 350,
    height: 370,
    addPosX: -130,
    addPosY: -380,
    tabbed: true,
    navPos: "bottom",
    navButtonReversed: false,
    disableSearch: false,
    hiddenScrollBar: true, // Not for Firefox
    animation: "slideDown",
    animationDuration: "1s",
    disableNav: false,
    emojiDim: {
        emojiPerRow: 5,
        emojiSize: 30,
        emojiButtonHeight: 80,
        hideCategory: false
    },
    // color: {
            // pickerBackground: "#181818",
            // searchBackground: "#202020",
            // foreground: "#fff",
            // navbarColor: "#000",
            // iconHoverColor: "",
            // borderColor: "",
            // searchBackground: "",
            // navbarColor: "",
            // navButtonHoverBG: "",
            // navButtonActiveBG: "",
            // navSvgFill: "",
            // closeMoveButtonColor: "",
    // }
    // navButtonSvg: {
            // button1: "",
            // button2: "",
            // button3: "",
            // button4: "",
            // button5: "",
            // button6: "",
            // button7: "",
            // button8: ``
    // }
    // addEmoji: {
    //     pickerTab: "a",
    //     customPickerTabIcon: ``,
    //     emoji: [
    //         {
    //             "emoji": "⚡",
    //             "title": "electronic"
    //         },
    //         {
    //             "emoji": "🚑",
    //             "title": "car"
    //         },
    //     ]
    // } && many more coming soon and available...
});

```



- Trigger :- (Array) Take an array of objects. Each object having selector and insertInto property.

    - selector :- (String) Take a button's id or class to make it as a popup button.

    - insertInto :- (Array or string) Take an input's or textarea's id or class to insert emojies.

- closeButton :- (Boolean) Hides or shows the close button.

- dragButton :- (Boolean) Hides or shows the drag button.

- width :- (Integer) Specifies width of picker.

- height :- (Integer) Specifies height of picker.

- addPosX :- (Integer) add the value to the X position of picker.

- addPosY :- (Integer) add the value to the Y position of picker.

- tabbed :- (Boolean) displays each section as tab, if true or as a single div.

- navPos :- ("bottom" || "top") specifies position of the navigation bar.

- navButtonReversed :- (Boolean) reverses order of buttons in nav bar.

- disableSearch :- (Boolean) disables search bar.

- hiddenScrollBar :- (Boolean) hides the scroll bar, if true, not for firefox.

- animation :- (String) takes popup, slideUp, slideDown, slideLeft, slideRight or fade.

- animationDuration :- (String) changes duration of popup animation, any css time compatible string.

- disableNav :- (Boolean) hides the navigation bar.

- emojiDim :- (Object) sets dimensions of emoji and related things.

    - emojiPerRow :- (Integer) defines how many in a row.

    - emojiSize :- (Integer) the size of emojies.

    - emojiButtonHeight :- (Integer) the height of emoji button.

    - hideCategory :- (Boolean) shows/hides the title of section.

## About Developer
Hi,

I am a 15 years old game, app and web developer. I started coding two years ago. Being bored by playing game all the time, One Day I thought to make games. 

[Check More Here](https://github.com/AnonymousXC)