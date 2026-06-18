local json = require("json")

while true do

    local state = {}

    state.playerX = memory.read_u16_le(0x02031DBC)
    state.playerY = memory.read_u16_le(0x02031DBE)

    local file = io.open("ipc/state.json", "w")

    file:write(json.encode(state))

    file:close()

    emu.frameadvance()

end