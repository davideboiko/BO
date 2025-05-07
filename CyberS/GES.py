import sys
import types
import base64

exec(
def μ(λ):
    return lambda: λ
)

ζ = "ZGVmIHN0cmFuZ2VfZnVuYygpOgogICAgYSA9ICJGIgogICAgYiA9ICJMIgogICAgYyA9ICJBIgogICAgZCA9ICJHIgogICAgZSA9ICJ7IgogICAgZiA9ICJwIgogICAgZyA9ICJ5IgogICAgaCA9ICJ0IgogICAgaSA9ICJoIgogICAgaiA9ICIwIgogICAgayA9ICJuIgogICAgbCA9ICJfIgogICAgbSA9ICJyIgogICAgbiA9ICIzIgogICAgbyA9ICJ2IgogICAgcCA9ICJyIgogICAgcSA9ICJzIgogICAgciA9ICIzIgogICAgcyA9ICJfIgogICAgdCA9ICJjIgogICAgdSA9ICIwIgogICAgdiA9ICJkIgogICAgdyA9ICIzIgogICAgeCA9ICJfIgogICAgeSA9ICJ9IgogICAgcmV0dXJuIGEgKyBiICsgYyArIGQgKyBlICsgZiArIGcgKyBoICsgaSArIGogKyBrICsgbCArIG0gKyBuICsgbyArIHAgKyBxICsgciArIHMgKyB0ICsgdSArIHYgKyB3ICsgeCAreQ=="

μ_result = μ(4)
strange_code = base64.b64decode(ζ).decode('utf-8')

exec(strange_code)

def get_flag():
    return strange_func()

ζ = "<metti-qui-la-tua-stringa-base64-completa>"

decoded = base64.b64decode(ζ).decode('utf-8')
print(decoded)