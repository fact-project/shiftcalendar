from .models import Role

STARTER = Role(
    name='Starter',
    title='performs the startup',
    color='DarkOrange',
    active=True,
    )

SHIFTER = Role(
    name='Shifter',
    title='recieves calls in the middle of the night',
    color="LightSeaGreen",
    active=True,
    )

PARKER = Role(
    name='Parker',
    title='performs the shutdown',
    color='PaleGreen',
    active=True,
    )

FALLBACK_SHIFTER = Role(
    name='Fallback_Shifter',
    title="gets all calls in case the real real shifter doesn't react",
    color="Red",
    active=True,
    )

FLARE_EXPERT = Role(
    name='Flare_Expert',
    title="receives calls in case of a flare",
    color="Black",
    active=True,
    )

FALLBACK_FLARE_EXPERT = Role(
    name='Fallback_Flare_Expert',
    title="gets calls in case the Flare_Expert doesn't react",
    color="Black",
    active=True,
    )

SHIFTER_AWAKE = Role(
    name='Shifter_Awake',
    title='pre 2017 standard shifter',
    color="DarkRed",
    active=False,
    )

DEBUG_SHIFT = Role(
    name='Debugging_Shift',
    title='pre 2017 standard debug shift',
    color="Green",
    active=False,
    )
