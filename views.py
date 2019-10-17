from flask import render_template

from route_helper import simple_route

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
    return render_template("mclaren.html", world=world)

@simple_route('/mclaren_key')
def mclaren_key(world: dict):
    for unit in world:
        if unit["Car Key"] == "McLaren":
            unit["Has Key"] = True
    return render_template("mclaren_key.html", world=world)

@simple_route('/lamborghini')
def lamborghini(world: dict):
    return render_template("lamborghini.html", world=world)

@simple_route('/ferrari')
def ferrari(world: dict):
    return render_template("ferrari.html", world=world)

@simple_route('/720s_test_drive')
def mclaren_test_drive(world: dict):
    return render_template("ferrari.html", world=world)

@simple_route('/goto/<where>/')
def open_door(world: dict, where: str) -> str:
    """
    Update the player location and encounter a monster, prompting the player
    to give them a name.

    :param world: The current world
    :param where: The new location to move to
    :return: The HTML to show the player
    """
    world['location'] = where
    return GAME_HEADER+ENCOUNTER_MONSTER.format(where)


@simple_route("/save/name/")
def save_name(world: dict, monsters_name: str) -> str:
    """
    Update the name of the monster.

    :param world: The current world
    :param monsters_name:
    :return:
    """
    world['name'] = monsters_name

    return GAME_HEADER+"""You are in {where}, and you are nearby {monster_name}
    <br><br>
    <a href='/'>Return to the start</a>
    """.format(where=world['location'], monster_name=world['name'])
