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
# This is the first page of the adventure. From here you can go down multiple different paths.
# This page displayes a picture of a showroom floor with different supercars
@simple_route('/showroom')
def showroom(world: dict):
    return render_template("showroom.html", world=world)

# This is the mclaren page. Here you acquire a catalytic converter, and it is added to your parts list.
# This page dislplays a picture of a McLaren 720s
@simple_route('/mclaren')
def mclaren(world: dict):
    if "Catalytic Converter" in world["Parts"]:
        pass
    else:
        world["Parts"].append("Catalytic Converter")
    return render_template("mclaren.html", world=world)

# This is the mclaren key page. On this page, you add a mclaren key and an alternator to your parts list.
# This page displays a picture of a set of keys to a mclaren and a link to take the Ferrari for a test drive
# If you click that link, you are redirected to 720s_test_drive.html
@simple_route('/mclaren_key')
def mclaren_key(world: dict):
    world["Has_McLaren_Key"] = True
    if "Alternator" in world["Parts"]:
        pass
    else:
        world["Parts"].append("Alternator")
    return render_template("mclaren_key.html", world=world)

# This page displays a picture of a Lamborghini
# You also add fuzzy dice to your parts list on this page
@simple_route('/lamborghini')
def lamborghini(world: dict):
    if "Fuzzy Dice" in world["Parts"]:
        pass
    else:
        world["Parts"].append("Fuzzy Dice")
    return render_template("lamborghini.html", world=world)

# This page displays a picture of a Ferrari collection
# You can then click a link to take you to pick up a ticket to see the Ferrari race
@simple_route('/ferrari')
def ferrari(world: dict):
    return render_template("ferrari.html", world=world)

# This page displays gif of McLaren 720s driving down the road
# You also add a battery to your parts list on this page
@simple_route('/720s_test_drive')
def mclaren_test_drive(world: dict):
    if "Battery" in world["Parts"]:
        pass
    else:
        world["Parts"].append("Battery")
    return render_template("720s_test_drive.html", world=world)

# This page displays a picture of ticket
# On this page you add a ticket to your parts list
@simple_route('/get_ticket')
def get_ticket(world: dict):
    if "Ticket" in world["Parts"]:
        pass
    else:
        world["Parts"].append("Ticket")
    world["Has_Ticket"] = True
    return render_template("get_ticket.html", world=world)

# On this page, a picture of snacks is displayed
# You get to this page if you click the link on the get_ticket.html page that says click here to get snacks
@simple_route('/get_snacks')
def get_snacks(world: dict):
    return render_template("get_snacks.html", world=world)

# This page displays a gif of Bart Simpson eating
# You are redirected to this page after you leave the get_snacks.html page
@simple_route('/eat_snacks')
def eat_snacks(world: dict):
    return render_template("eat_snacks.html", world=world)

# This page displays a gif of a Ferrari racing
# You are redirected to this page if you click the link on get_ticket.html that says click here to see the race
@simple_route('/ferrari_race')
def ferrari_race(world: dict):
    return render_template("ferrari_race.html", world=world)

# If your parts list matches the list of required items, this function directs you to page that says congratulations
# and gives you a prize.
# If your parts list does not match the list of required items exactly, then you are directed to a page that says
# you still need to get more items so you can get a prize. Then it directs you back to the showroom. 
@simple_route('/prize')
def prize(world: dict):
    needed_items = ["Catalytic Converter", "Alternator", "Battery", "Fuzzy Dice", "Ken Block Autograph", "Ticket"]
    needed_items.sort()
    world["Parts"].sort()
    if world["Parts"] == needed_items:
        return render_template("prize.html", world=world)
    else:
        return render_template("need_more_items.html", world=world)

# This function saves input from the drop menu that asks if you want to see a Lamborghini racing
# If you choose yes, the function send syou to lamborghini_track.html. If you choose no, it sends you to showroom.html.
@simple_route('/save/')
def save_laborghini_track(world: dict, *args) -> str:
    world["Race_Status"] = request.values.get("race")
    if world["Race_Status"] == "Yes":
        return render_template("lamborghini_track.html")
    else:
        return render_template("showroom.html")

# This function saves input from the drop menu that asks if you want an autograph from Ken Block
# If you choose yes, the function sends you to the ken_block.html. If you choose no, it sends you back to showroom.html
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


