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
	{ 0x92997ed8, "_printk" },
	{ 0xe3ec2f2b, "alloc_chrdev_region" },
	{ 0x7636e2b6, "cdev_init" },
	{ 0xc77ea9f2, "cdev_add" },
	{ 0x6091b333, "unregister_chrdev_region" },
	{ 0xb88a2432, "cdev_del" },
	{ 0x38022ea8, "module_layout" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "8A5909DC602C6135DF4316F");
