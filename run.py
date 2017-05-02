from exercise import Path

p = Path('/home/hello/moto')
assert p.current_path == '/home/hello/moto'
p.cd('../kitty')
assert p.current_path == '/home/hello/kitty'
p.cd('/home/')
assert p.current_path == '/home'
