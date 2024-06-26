# Fremony at the library
# 7.5.2024

def fremony(A,B):
    C = A[-22:]
    B = "\n" + B

    output = (A + B + C +
              B[:63] + C[:9] + C[:8] + C[:22] +
              B[:8] + C + B[:2] + C[:10] + C +
              B[:3] + C[:1] + C[:11] + C[:16] + C[:19] + C +
              B[:4] + C +
              B[:48] + C[:7] + C[:1] + C[:16] + C[:8] + C[:17] + C[:9] + C[:11] + C +
              B[:1] + C[:4] + C[:1] + C + C +
              B +
              "n he latched onto a through ball. Although he was hauled down by the 'keeper "
              "he still managed to stroke the ball home.\nBut for the second week running Durant "
              "had to leave the field injured, this time suffering eye trouble.\nThe winning goal "
              "was another 25-yard shot - again from Blackstones' central defender - coming from "
              "their second chance of the game.\nGary Cooper, recently signed from Queens Old Boys, "
              "had a good debut.")

    return output



if __name__ == "__main__":

    A = "It was a bright cold day in April, and the clocks were striking thirteen."
    B = "Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."

    print(fremony(A,B))