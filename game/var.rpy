

define narrator = Character(None,nvl_narrator,ctc="ctc_turtle",ctc_position="nestled",ctc_pause ="ctc_turtle")

image ctc_turtle = Animation(
"gui/ani_turtle1.png", 0.2, #The second number is the time that Ren'Py stays on this one image
"gui/ani_turtle2.png", 0.2,
"gui/ani_turtle3.png", 0.2,
"gui/ani_turtle4.png", 0.2,
ctc_position="nestled") #The position of the CTC, adjust for your own nee

image ctc_nvl2 = Animation(
"gui/button_arrowr1.png", 0.2,
"gui/button_arrowr2.png", 0.2,
"gui/button_arrowr3.png", 0.2,
"gui/button_arrowr4.png", 0.2,
"gui/button_arrowr5.png", 0.2,
ctc_position = "nestled"
)
