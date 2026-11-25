#include <linux/module.h>
#include <linux/export-internal.h>
#include <linux/compiler.h>

MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};



static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x61eb329b, "gpiod_set_value" },
	{ 0x92997ed8, "_printk" },
	{ 0xb558baa4, "gpio_to_desc" },
	{ 0xc9986daf, "gpiod_direction_output" },
	{ 0x659a0e71, "gpiod_direction_input" },
	{ 0x97f01b96, "gpiod_get_value" },
	{ 0x38022ea8, "module_layout" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "9B7ADA009418E0A5D17FF72");
