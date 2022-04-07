while True:
    try:
        import time
        time.sleep(2)
    except KeyboardInterrupt:
        print("can't kill me!")
