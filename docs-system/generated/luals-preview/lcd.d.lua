---@meta

---@class lcd
lcd = {}

--- Display a previously opened bitmap at coordinates and optionally scale it.
--- @since 2.3.0
---@param bitmap bitmapPointer Pointer returned by Bitmap.open().
---@param x integer Top coordinate.
---@param y integer Left coordinate.
---@param scale? integer Scale percent where 100 keeps original size.
function lcd.drawBitmap(bitmap, x, y, scale) end
