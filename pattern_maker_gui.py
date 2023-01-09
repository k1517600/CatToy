import os

import dearpygui.dearpygui as dpg
from pattern_maker import *

class UIHandler:

    def __init__(self):
        self.current_pattern: Pattern
        self.make_gui()

    def make_gui(self):
        dpg.create_context()
        dpg.create_viewport(title='Cat Toy Pattern Creator!!!', width=800, height=500)

        with dpg.font_registry():
            header_font = dpg.add_font("proggy-clean.ttf", 30)
            subheader_font = dpg.add_font("proggy-clean.ttf", 20)

        with dpg.texture_registry():
            for filename in os.listdir("images"):
                width, height, channels, data = dpg.load_image("images/" + filename)
                texture_id = dpg.add_static_texture(width, height, data, tag=filename)

        with dpg.window(tag="Cat Toy Pattern Creator!!!"):
            # text
            title = dpg.add_text("AlrightyTighty's \nCattern Maker!!", pos=(500, 50))
            subtitle = dpg.add_text("By Joshua Novak, 2023", pos=(500, 120))
            dpg.bind_item_font(title, header_font)
            dpg.bind_item_font(subtitle, subheader_font)

            # main image
            dpg.add_image(texture_tag="MainMenuCat.png", pos=(0, 210))

            # buttons
            dpg.add_image_button(texture_tag="NewPattern.png", pos=(600, 170), callback=self.__new_pattern)
            dpg.add_image_button(texture_tag="LoadPattern.png", pos=(600, 300))
            # menu bar
            with dpg.menu_bar():
                with dpg.menu(label="File"):
                    dpg.add_menu_item(label="Save")
                    dpg.add_menu_item(label="Save As")
                    dpg.add_menu_item(label="New Pattern")

                with dpg.menu(label="Edit"):
                    dpg.add_menu_item(label="Undo")
                    dpg.add_menu_item(label="Redo")
                    dpg.add_menu_item(label="Paste")
                    dpg.add_menu_item(label="Copy")

            dpg.set_primary_window("Cat Toy Pattern Creator!!!", True)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def __new_pattern(self):
        pass


