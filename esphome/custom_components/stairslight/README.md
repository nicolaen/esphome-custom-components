# Stairs light effect
This component provides a simple light effect for your stairs addressable LEDs

## Example configuration
Example configuration for turning on the leds with the `stairslight` light effect via a script:

```yaml
api:
  services: 
    - service: play_step_by_step
      then:
        - script.execute: play_step_by_step

script:
  - id: play_step_by_step
    mode: single
    then:
      - light.control:
          id: stairs_leds
          state: on
          effect: Step by step
          red: 1
          green: 1
          blue: 1

stairslight:

light:
  - platform: neopixelbus
    num_leds: 300
    variant: WS2812X
    name: LEDs
    id: stairs_leds
    type: GRB
    pin: D6
    default_transition_length: 
      milliseconds: 10
    effects:
      - stairslight:
          name: Step by step
          update_interval: 200ms
          steps:
            - start: 0
              end: 29
            - start: 30
              end: 59
            - start: 60
              end: 89
            - start: 90
              end: 119
            - start: 120
              end: 149
            - start: 150
              end: 179
            - start: 180
              end: 209
            - start: 210
              end: 239
            - start: 240
              end: 269
            - start: 270
              end: 299
```