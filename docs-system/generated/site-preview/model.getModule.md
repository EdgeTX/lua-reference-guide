# model.getModule

`model.getModule(index)`

Get RF module parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `index` | yes | `integer` | module index (0 for internal, 1 for external) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | requested module does not exist |
| `-` | `table` | module parameters: * `subType` (number) protocol index  * `modelId` (number) receiver number  * `firstChannel` (number) start channel (0 is CH1)  * `channelsCount` (number) number of channels sent to module  * `Type` (number) module type  * if the module type is Multi additional information are available  * `protocol` (number) protocol number (Multi only)  * `subProtocol` (number) sub-protocol number (Multi only)  * `channelsOrder` (number) first 4 channels expected order (Multi only)  * if the module type is LemonDSMP additional info is available  * `channelsOrder` (number) first 4 channels expected order (DSMP only) |

## Availability

- Since: `2.2.0`
- Radio support: `all`

## Notes

- `Type` values:
  * 0 NONE
  * 1 PPM
  * 2 XJT_PXX1
  * 3 ISRM_PXX2
  * 4 DSM2
  * 5 CROSSFIRE
  * 6 MULTIMODULE
  * 7 R9M_PXX1
  * 8 R9M_PXX2
  * 9 R9M_LITE_PXX1
  * 10 R9M_LITE_PXX2
  * 11 R9M_LITE_PRO_PXX1
  * 12 R9M_LITE_PRO_PXX2
  * 13 SBUS
  * 14 XJT_LITE_PXX2
  * 15 MODULE_TYPE_FLYSKY_AFHDS3,
  * 16 ??
  * 17 MODULE_TYPE_LEMON_DSMP

`subType` values for XJT_PXX1:
 * -1 OFF
 * 0 D16
 * 1 D8
 * 2 LR12

## Source

`radio/src/lua/api_model.cpp`
