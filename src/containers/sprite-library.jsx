import bindAll from 'lodash.bindall';
import PropTypes from 'prop-types';
import React from 'react';
import {injectIntl, intlShape, defineMessages} from 'react-intl';
import VM from 'scratch-vm';

import spriteLibraryContent from '../lib/libraries/sprites.json';
import randomizeSpritePosition from '../lib/randomize-sprite-position';
import spriteTags from '../lib/libraries/sprite-tags';

import LibraryComponent from '../components/library/library.jsx';

const messages = defineMessages({
    libraryTitle: {
        defaultMessage: 'Choose a Sprite',
        description: 'Heading for the sprite library',
        id: 'gui.spriteLibrary.chooseASprite'
    }
});

class SpriteLibrary extends React.PureComponent {
    constructor (props) {
        super(props);
        bindAll(this, [
            'handleItemSelect'
        ]);
    }
    handleItemSelect (item) {
        // Randomize position of library sprite
        randomizeSpritePosition(item);
        this.props.vm.addSprite(JSON.stringify(item.json)).then(() => {
            this.props.onActivateBlocksTab();
        });
    }
    render () {

        //tarmelop hack: filter sprite library content   
        var microworld = false;
        if (microworld){
            var allSprites = this.state.sprites;
            var microworldSprites = ['Apple', 'Ball', 'Beetle'];
            var filteredSprites = [];
            var i;
            for(i=0; i<allSprites.length; i++){
                if(microworldSprites.includes(allSprites[i].name)){
                    filteredSprites.push(allSprites[i]);
                }
            }
            this.state.sprites = filteredSprites;
        }

        return (
            <LibraryComponent
                data={spriteLibraryContent}
                id="spriteLibrary"
                tags={spriteTags}
                title={this.props.intl.formatMessage(messages.libraryTitle)}
                onItemSelected={this.handleItemSelect}
                onRequestClose={this.props.onRequestClose}
            />
        );
    }
}

SpriteLibrary.propTypes = {
    intl: intlShape.isRequired,
    onActivateBlocksTab: PropTypes.func.isRequired,
    onRequestClose: PropTypes.func,
    vm: PropTypes.instanceOf(VM).isRequired
};

export default injectIntl(SpriteLibrary);
