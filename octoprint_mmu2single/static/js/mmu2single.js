/*
 * View model for OctoPrint-MMU2Single
 *
 * Author: lcworld
 * License: AGPLv3
 */
$(function() {
    function Mmu2singleViewModel(parameters) {
        var self = this;

        self.settings = parameters[0];

        self.nbFilaments = ko.observable();
        // push form modifications to settings
        self.nbFilaments.subscribe(function(newValue) {
            self.settings.settings.plugins.mmu2single.nbFilaments(newValue);
            self.refreshNBFilaments();              
        });

        self.filamentsList = ko.observableArray();

        self.filamentToUse = ko.observable();
        // push form modifications to settings
        self.filamentToUse.subscribe(function(newValue) {
            if (newValue !== undefined) {
                self.settings.settings.plugins.mmu2single.filamentToUse(newValue);
            }
        });

        // refresh list of filaments
        self.refreshNBFilaments = function () {
            // get nb of filament
            var f = self.settings.settings.plugins.mmu2single.nbFilaments();

            // get current filament
            var s = self.settings.settings.plugins.mmu2single.filamentToUse();
            // if not in nb of filament, set filament to use as first one (0 based)
            if (0 > s || s > (f-1) ) {
                s=0;
            }
            
            // clean list and reinsert all new filaments
            // text of operation defined in template
            self.filamentsList.removeAll();            
            for (var i=0 ; i < f ; i++) {
                self.filamentsList.push(i);
            }

            // set current filament back
            self.filamentToUse(s);
        };

        self.onBeforeBinding = function() {
            //console.log(self.settings.settings.plugins.mmu2single.nbFilaments());
            self.nbFilaments(self.settings.settings.plugins.mmu2single.nbFilaments());
            self.refreshNBFilaments();
        }
    }

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: Mmu2singleViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies: [ "settingsViewModel" ],
        // Elements to bind to, e.g. #settings_plugin_mmu2single, #tab_plugin_mmu2single, ...
        elements: [ "#settings_plugin_mmu2single" ]
    });
});
