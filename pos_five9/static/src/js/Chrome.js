odoo.define('pos_five9.chrome', function (require) {
    'use strict';

    const Chrome = require('point_of_sale.Chrome');
    const Registries = require('point_of_sale.Registries');

    const PosFiveChrome = (Chrome) =>
        class extends Chrome {
            /**
             * @override
             * Set partner from url as started selected partner
             */
            get startScreen() {
                var result = super.startScreen;
                var given_partner = new RegExp('[\?&]partner_id=([^&#]*)').exec(window.location.href);
                var partner_id = given_partner && given_partner[1] && parseInt(given_partner[1]) || false;
                if (partner_id) {
                    var currentOrder = this.env.pos.get_order();
                    var newClient = this.env.pos.db.get_partner_by_id(partner_id);
                    currentOrder.set_client(newClient);
                    currentOrder.updatePricelist(newClient);
                }
                return result;
            }
        };

    Registries.Component.extend(Chrome, PosFiveChrome);
    return Chrome;
});
