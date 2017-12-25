while(True):
    import time
    from try_block import *

    try:
        app_v2()
        print('Success!')

    except:
        print('Sorry let me check again in 3 seconds')

    time.sleep(3)
