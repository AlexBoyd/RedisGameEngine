from redis import StrictRedis
import os

if __name__ == "__main__":
    redis = StrictRedis(host='redis')
    actions = {}

    for fn in os.listdir('./src/Actions'):
        print(fn)
        with open("./src/Actions/{fn}".format(fn=fn)) as f:
            actions[fn] = redis.register_script(f.read())

    print(actions.items())
    print(redis.hgetall('game_state'))

    