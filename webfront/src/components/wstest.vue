<template>
    <div>
        123
    </div>
</template>

<script type="text/javascript">
export default {
    name: "test",
    data() {
        return {
            sendmsg:"",
        }
    },
    created() {
        this.$axios.get('/api/city1/').then(response => {
            this.config1 = response.data.data
        })
        this.$axios.get('/api/city2/').then(response => {
            this.config2 = response.data.data
        })
    },
};
</script>

<style>
html,body{
    margin: 0;
    padding: 0;
}

</style>