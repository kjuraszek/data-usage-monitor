<template>
  <div>
    <p class="text-h6">
        Checked  at {{ currentTimeStamp }}
    </p>
    <v-simple-table>
        <tbody>
        <tr>
            <td>Download</td>
            <td>{{ currentMonthDownload }}</td>
        </tr>
        <tr>
            <td>Upload</td>
            <td>{{ currentMonthUpload }}</td>
        </tr>
        <tr>
            <td>Total</td>
            <td>{{ totalUsage }}</td>
        </tr>
        </tbody>
    </v-simple-table>
    </div>
</template>

<script>
import moment from 'moment'
  
export default {
    name: 'UsageDataTable',
    computed: {
      currentMonthDownload () {
        return parseFloat(this.$store.state.currentMonthDownload).toFixed(3)
      },
      currentMonthUpload () {
        return parseFloat(this.$store.state.currentMonthUpload).toFixed(3)
      },
      currentTimeStamp () {
        return this.formatDate(this.$store.state.currentTimeStamp)
      },
      totalUsage () {
        return this.calculateUsage(this.currentMonthDownload, this.currentMonthUpload)
      },
    },
    methods: {
      formatDate (date) {
        return moment(date).format('D-M-YYYY, HH:mm:ss')
      },
      calculateUsage (download, upload) {
        return parseFloat(parseFloat(download) + parseFloat(upload)).toFixed(3)
      }
    }
}
</script>