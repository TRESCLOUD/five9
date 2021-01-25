odoo.define('pos_five9.ClientListScreen', function(require) {
    'use strict';

    const ClientListScreen = require('point_of_sale.ClientListScreen');
    const Registries = require('point_of_sale.Registries');

    const PosFiveClientListScreen = ClientListScreen =>
        class extends ClientListScreen {
            constructor() {
                super(...arguments);
                this.state.editModeProps = {
                    partner: this.props.client,
                };
                this.state.detailIsShown = true;
            }
        };

    Registries.Component.extend(ClientListScreen, PosFiveClientListScreen);
    return ClientListScreen;
});
