#pragma once

#include "esphome/core/component.h"
#include "esphome/components/light/addressable_light_effect.h"

#include <vector>

namespace esphome {
namespace stairslight {

struct StepLedsRange
{
  uint16_t start;
  uint16_t end;
};

class StairslightLightEffect : public light::AddressableLightEffect {
 public:
  StairslightLightEffect(const std::string &name, const uint32_t update_interval);

  void start() override;
  void apply(light::AddressableLight &it, const Color &current_color) override;

  void set_steps(const std::vector<StepLedsRange> &steps);

 protected:
  uint32_t step;
  uint32_t update_interval;
  uint32_t switch_off_delay;
  uint32_t last_run{0};
  std::vector<StepLedsRange> step_leds;
};

}  // namespace stairslight
}  // namespace esphome
