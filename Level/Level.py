import json
from Sprite.NonAlive.Tile import Tile
from Sprite.Alive.Character import Character

def load_level(level):
    tiles = load_tiles(level)
    enemies = load_enemies(level)
    return tiles, enemies
        
        
def load_tiles(level):
    tiles = []
    with open("Level/" + level + "/tiles.json") as tiles_file:
        tiles_json = json.loads(tiles_file.read())
        for tile in tiles_json:
            color = (tile["color"][0], tile["color"][1], tile["color"][2])
            tiles.append(Tile(tile["x"], tile["y"], tile["width"], tile["height"], color))
    return tiles

def load_enemies(level):
    enemies = []
    with open("Level/" + level + "/enemies.json") as enemies_file:
        enemies_json = json.loads(enemies_file.read())
        for enemy in enemies_json:
            color = (enemy["color"][0], enemy["color"][1], enemy["color"][2])
            enemies.append(Character(enemy["x"], enemy["y"], enemy["width"], enemy["height"], color, enemy["speed_x"], enemy["speed_y"]))
    return enemies