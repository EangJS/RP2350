#include <stdio.h>
#include "SEGGER_RTT.h"
#include "RP2350.h"
#include "core_cm33.h"

int main() {
    CoreDebug->DEMCR |= CoreDebug_DEMCR_TRCENA_Msk;
    uint32_t i = 0;
    while ( 1 )
    {
        SEGGER_RTT_printf(0, "%d, Hello, world!\n", i++);
        for (int i = 0; i < 1000000; i++) {
            // do nothing
        }
    }
    return 0;
}
