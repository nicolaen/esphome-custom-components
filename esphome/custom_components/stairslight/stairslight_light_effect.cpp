#include "stairslight_light_effect.h"
#include "esphome/core/log.h"

namespace esphome {
namespace stairslight {

static const char *const TAG = "stairslight_light_effect";

StairslightLightEffect::StairslightLightEffect(const std::string &name, const uint32_t update_interval, const uint32_t switch_off_delay) : AddressableLightEffect(name), update_interval(update_interval) {}

void StairslightLightEffect::set_steps(const std::vector<StepLedsRange> &steps) {
  step_leds = steps;
}

void StairslightLightEffect::start() {
  AddressableLightEffect::start();

  step = 0;
}

void StairslightLightEffect::apply(light::AddressableLight &it, const Color &current_color) {
  const uint32_t now = millis();
  if (now - last_run < update_interval || step == step_leds.size()) {
    return;
  }

  last_run = now;

  it.range(step_leds[step].start, step_leds[step].end) = current_color;
  it.schedule_show();

  step++;
}

}  // namespace stairslight
}  // namespace esphome
