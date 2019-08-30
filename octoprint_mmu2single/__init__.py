# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class MMU2SinglePlugin(octoprint.plugin.StartupPlugin,
					   octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin,
                       octoprint.plugin.TemplatePlugin):
	##~~ log settings on startup
	def on_after_startup(self):
		self._logger.info("nbFilaments: %d" % self._settings.get_int(["nbFilaments"]))
		self._logger.info("filamentToUse: %d" % self._settings.get_int(["filamentToUse"]))

	##~~ SettingsPlugin mixin
	def get_settings_defaults(self):
		return dict(
			nbFilaments=5,
			filamentToUse=0
		)

	##~~ AssetPlugin mixin
	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/mmu2single.js"],
			css=["css/mmu2single.css"],
			less=["less/mmu2single.less"]
		)

	##~~ Softwareupdate hook
	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			mmu2single=dict(
				displayName="MMU2Single Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="lcworld",
				repo="OctoPrint-MMU2Single",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/lcworld/OctoPrint-MMU2Single/archive/{target_version}.zip"
			)
		)

	##~~ Define templates
	def get_template_configs(self):
		return [
			# dict(type="navbar", custom_bindings=False),
			dict(type="settings", custom_bindings=True)
		]


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "MMU2Single Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = MMU2SinglePlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

