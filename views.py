from flask import render_template

from route_helper import simple_route

from flask import request

GAME_HEADER = """
<h1>Welcome to adventure quest!</h1>
<p>At any time you can <a href='/reset/'>reset</a> your game.</p>
"""


@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    return render_template("index.html")


ENCOUNTER_MONSTER = """
<!-- Curly braces let us inject values into the string -->
You are in {}. You found a monster!<br>

<!-- Image taken from site that generates random Corgi pictures-->
<img src="http://placecorgi.com/260/180" /><br>
    
What is its name?

<!-- Form allows you to have more text entry -->    
<form action="/save/name/">
    <input type="text" name="player"><br>
    <input type="submit" value="Submit"><br>
</form>
"""
@simple_route('/showroom')
def showroom(world: dict):
    return render_template("showroom.html", world=world)

@simple_route('/mclaren')
def mclaren(world: dict):
    if "Catalytic Converter" in world["Parts"]:
        pass
    else:
        world["Parts"].append("Catalytic Converter")
    return render_template("mclaren.html", world=world)

@simple_route('/mclaren_key')
def mclaren_key(world: dict):
    world["Has_McLaren_Key"] = True
    if "Alternator" in world["Parts"]:
        pass
    else:
        world["Parts"].append("Alternator")
    return render_template("mclaren_key.html", world=world)

@simple_route('/lamborghini')
def lamborghini(world: dict):
    if "Fuzzy Dice" in world["Parts"]:
        pass
    else:
        world["Parts"].append("Fuzzy Dice")
    return render_template("lamborghini.html", world=world)

@simple_route('/ferrari')
def ferrari(world: dict):
    return render_template("ferrari.html", world=world)

@simple_route('/720s_test_drive')
def mclaren_test_drive(world: dict):
    if "Battery" in world["Parts"]:
        pass
    else:
        world["Parts"].append("Battery")
    return render_template("720s_test_drive.html", world=world)

@simple_route('/get_ticket')
def get_ticket(world: dict):
    if "Ticket" in world["Parts"]:
        pass
    else:
        world["Parts"].append("Ticket")
    world["Has_Ticket"] = True
    return render_template("get_ticket.html", world=world)

@simple_route('/ferrari_race')
def ferrari_race(world: dict):
    return render_template("ferrari_race.html", world=world)

@simple_route('/prize')
def prize(world: dict):
    return render_template("prize.html", world=world)

@simple_route('/save/')
def save_laborghini_track(world: dict, *args) -> str:
    world["Race_Status"] = request.values.get("race")
    if world["Race_Status"] == "Yes":
        return render_template("lamborghini_track.html")
    else:
        return render_template("showroom.html")

@simple_route('/save/ken_block/')
def save_ken_block(world: dict, *args) -> str:
    world["ken_block_autograph"] = request.values.get("signature?")
    if world["ken_block_autograph"] == "Yes":
        if "Ken Block Autograph" in world["Parts"]:
            pass
        else:
            world["Parts"].append("Ken Block Autograph")
        return render_template("ken_block.html", world=world)
    else:
        return render_template("showroom.html")


