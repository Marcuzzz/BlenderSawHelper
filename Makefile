FILE_TO_COPY := MySawHelper.py
BLENDER_VERSION := 3.2

ifeq ($(shell uname),Darwin)
	DEST_DIR := /Users/$(shell whoami)/Library/Application Support/Blender/$(BLENDER_VERSION)/scripts/addons/
endif

ifeq ($(shell uname),Linux)
	DEST_DIR := /home/$(shell whoami)/.config/blender/$(BLENDER_VERSION)/scripts/addons/
endif

ifeq ($(shell uname),Linux)
	DEST_DIR := C:/Users/$(USERNAME)/AppData/Roaming/Blender Foundation/Blender/$(BLENDER_VERSION)/scripts/addons/
endif

.PHONY: install
install:
# @echo "$(DEST_DIR)"
	cp $(FILE_TO_COPY) "$(DEST_DIR)"

.PHONY: clean
clean:
	@echo "Hello, $(DEST_DIR)"
	rm "$(DEST_DIR)/$(FILE_TO_COPY)"