import fire

def hello(name="World22"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)