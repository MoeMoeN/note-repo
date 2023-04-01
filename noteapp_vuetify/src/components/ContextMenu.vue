<template>
    <v-menu
    v-model="showMenu"
    absolute
    :close-on-content-click="false"
    offset-x
    :style="{ top: `${y}px`, left: `${x}px`}"
    >
        <v-list >
            <v-list-item
            v-for="(item, index) in items"
            :key="index"
            @click="onItemClick(item)"
            >
                <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
        </v-list>
    </v-menu>
</template>

<script>
export default {
    props: {
        x: Number,
        y: Number,
        items: Array
    },
    data() {
        return{
            showMenu: false,

        }
    },
    methods: {
        onItemClick(item) {
            this.showMenu = false;
            this.$emit('item-click', item);
        }
    }
}
</script>