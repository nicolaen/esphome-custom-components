import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components.light.types import AddressableLightEffect
from esphome.components.light.effects import register_addressable_effect
from esphome.const import CONF_NAME, CONF_UPDATE_INTERVAL

CONF_SWITCH_OFF_DELAY = "switch_off_delay"
CONF_STEPS = "steps"
CONF_START = "start"
CONF_END = "end"

stairslight_ns = cg.esphome_ns.namespace("stairslight")
StairslightLightEffect = stairslight_ns.class_(
    "StairslightLightEffect", AddressableLightEffect
)
StepLedsRange = stairslight_ns.struct("StepLedsRange")

CONFIG_SCHEMA = cv.Schema({})


@register_addressable_effect(
    "stairslight",
    StairslightLightEffect,
    "Stairslight",
    {
        cv.Required(CONF_NAME): cv.string_strict,
        cv.Optional(
            CONF_UPDATE_INTERVAL, default="100ms"
        ): cv.positive_time_period_milliseconds,
        cv.Optional(
            CONF_SWITCH_OFF_DELAY, default="5000ms"
        ): cv.positive_time_period_milliseconds,
        cv.Optional(
            CONF_STEPS, default=[{CONF_START: 0, CONF_END: 10}, {CONF_START: 10, CONF_END: 20}]
        ): cv.ensure_list(
            {
                cv.Required(CONF_START): cv.positive_int,
                cv.Required(CONF_END): cv.positive_int,
            },
        ),
    },
)
async def stairslight_light_effect_to_code(config, effect_id):
    effect = cg.new_Pvariable(
        effect_id, config[CONF_NAME],
        config[CONF_UPDATE_INTERVAL], config[CONF_SWITCH_OFF_DELAY]
    )
    steps = []
    for step in config.get(CONF_STEPS, []):
        steps.append(
            cg.StructInitializer(
                StepLedsRange,
                ("start", int(step[CONF_START])),
                ("end", int(step[CONF_END] + 1)),
            )
        )
    cg.add(effect.set_steps(steps))
    return effect

