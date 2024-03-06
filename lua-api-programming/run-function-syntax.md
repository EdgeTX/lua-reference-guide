# Run Function Syntax

The run function is the function that is periodically called for the lifetime of script execution. Syntax of the run function is different between [mix scripts](../part\_i\_-\_script\_type\_overview/mix.md) and [telemetry scripts](../part\_i\_-\_script\_type\_overview/telemetry.md).

## Run Function for Mix Scripts

```lua
local function <run_function_name>([first input, [second input], …])

   -- if mix has no return values
   return

   -- if mix has two return values
   return value1, value2

end
```

*   **Input parameters:**

    zero or more input values, their names are arbitrary, their meaning and order is defined by the input table. (see [Input Table Syntax](run-function-syntax.md))
* **Return values:**
  *   none - if output table is empty (i.e. script has no output)

      values

      * or -
  * comma separated list of output values, their order and meaning is defined by the output table. (see [Output Table Syntax](run-function-syntax.md))

## Run Function for Telemetry Scripts

```lua
local function <run_function_name>(key-event)
  return 0 -- values other than zero will halt the script
end
```

*   **Input parameters:**

    The _key-event_ parameter indicates which transmitter button has been pressed (see [Key Events](broken-reference))
*   **Return values:**

    A non-zero return value will halt the script
