---@meta

---@class Bitmap
Bitmap = {}

--- Return width, height of a bitmap object
--- @since 2.2.0
---@param name pointer point to a bitmap previously opened with Bitmap.open()
---@return integer width_in_pixels
---@return integer height_in_pixels
function Bitmap.getSize(name) end

--- Loads a bitmap in memory, for later use with lcd.drawBitmap(). Bitmaps should be loaded only
once, returned object should be stored and used for drawing. If loading fails for whatever
reason the resulting bitmap object will have width and height set to zero.
--- @since 2.2.0
---@param name string full path to the bitmap on SD card (i.e. “/IMAGES/test.bmp”)
---@return object bitmap
function Bitmap.open(name) end

--- Return a resized bitmap object
--- @since 2.8.0
---@param bitmap pointer point to a bitmap previously opened with Bitmap.open()
---@param width integer the new bitmap width
---@param height integer the new bitmap height
function Bitmap.resize(bitmap, width, height) end

--- Return a 8bit bitmap mask that can be used with lcd.drawBitmapPattern()
--- @since 2.8.0
---@param bitmap pointer point to a bitmap previously opened with Bitmap.open()
---@return unknown a
function Bitmap.toMask(bitmap) end
