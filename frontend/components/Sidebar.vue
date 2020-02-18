<template>
    <div class="bg-gray-700 shadow-lg h-24 fixed pin-b md:relative md:h-screen z-10 w-full md:w-48">
        <div class="md:mt-12 md:w-48 md:fixed md:pin-l md:pin-t content-center md:content-start text-left justify-between">
            <h1 class="text-xl text-white md:px-2 "> <a href="/">Nama Perusahaan</a> </h1>
            <ul class="list-reset flex flex-row md:flex-col py-0 md:py-3 px-1 md:px-2 text-center md:text-left">
                <!-- Dashboard -->
                <li class="mr-3 flex-1" v-if="enabled_feature('Dashboard')">
                    <a href="/dashboard" class="block py-1 md:py-3 pl-1 align-middle text-white no-underline hover:text-white border-b-2 border-grey-darkest hover:border-pink hover:bg-gray-600">
                        <i class="fas fa-tasks pr-0 md:pr-3"></i><span class="pb-1 md:pb-0 text-xs md:text-base text-grey-dark md:text-grey-light block md:inline-block">Dashboard</span>
                    </a>
                </li>
                <!-- User Management -->
                <li class="mr-3 flex-1" v-if="enabled_feature('UserManagement')">
                    <a href="/user-management" class="block py-1 md:py-3 pl-1 align-middle text-white no-underline hover:text-white border-b-2 border-grey-darkest hover:border-pink hover:bg-gray-600">
                        <i class="fas fa-tasks pr-0 md:pr-3"></i><span class="pb-1 md:pb-0 text-xs md:text-base text-grey-dark md:text-grey-light block md:inline-block">User Management</span>
                    </a>
                </li>
                <!-- Transaction -->
                <li class="mr-3 flex-1" v-if="enabled_feature('Transaction')">
                    <a href="#" class="block py-1 md:py-3 pl-1 align-middle text-white no-underline hover:text-white border-b-2 border-grey-darkest hover:border-purple hover:bg-gray-600">
                        <i class="fa fa-envelope pr-0 md:pr-3"></i><span class="pb-1 md:pb-0 text-xs md:text-base text-grey-dark md:text-grey-light block md:inline-block">Transaction</span>
                    </a>
                </li>
                <!-- Ticketing System -->
                <li class="mr-3 flex-1" v-if="enabled_feature('TicketingSystem')">
                    <a href="/ticket" class="block py-1 md:py-3 pl-1 align-middle text-white no-underline hover:text-white border-b-2 border-blue-dark hover:bg-gray-600">
                        <i class="fas fa-chart-area pr-0 md:pr-3 text-blue-dark"></i><span class="pb-1 md:pb-0 text-xs md:text-base text-white md:text-white block md:inline-block">Ticketing System</span>
                    </a>
                </li>
                <!-- Server Monitoring -->
                <li class="mr-3 flex-1" v-if="enabled_feature('ServerMonitoring')">
                    <a href="#" class="block py-1 md:py-3 pl-0 md:pl-1 align-middle text-white no-underline hover:text-white border-b-2 border-grey-darkest hover:border-red hover:bg-gray-600">
                        <i class="fa fa-wallet pr-0 md:pr-3"></i><span class="pb-1 md:pb-0 text-xs md:text-base text-grey-dark md:text-grey-light block md:inline-block">Server Monitoring</span>
                    </a>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            feature_list: JSON.parse(localStorage.feature_list)
        }
    },
    mounted(){
        if (!this.feature_list) {
            return this.$router.push('/')
        }
    },
    methods: {
        enabled_feature: function (feature){
            return this.feature_list.find(item => item.flagName === feature)
        }
    }
}
</script>
