paper = True
lead = True
lead_out = True



def use_pencil(paper, lead, lead_out):
    if not paper:
        print("Go get paper.")
    elif not lead:
        print("Go get lead.")
    elif not lead_out:
        print("Push lead out of pencil.")
    else:
        print("You used pencil.")


use_pencil(True, True, True)
use_pencil(False, True, True)
use_pencil(True, False, True)
use_pencil(True, True, False)


