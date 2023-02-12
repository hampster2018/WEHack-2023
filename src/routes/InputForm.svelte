<script>
    import {Label, Input, Select, Checkbox, Button} from 'flowbite-svelte'

    /**
	 * @type {any}
	 */
    let descSelected;
    /**
	 * @type {any}
	 */
    let citySelected;

    /**
     * @type {HTMLDivElement}
     */
    let form;

    let useDescCodes = [
    {value: 'Commercial', name: 'Commercial'},
    {value: 'Commercial Office', name: 'Commercial Office'},
    {value: 'Commercial Store', name: 'Commercial Store'},
    {value: 'Industrial', name: 'Industrial'},
    {value: 'Unzoned', name: 'Unzoned'},
    {value: 'Residential', name: 'Residential'},
    {value: 'Single Residential', name: 'Single Residential'},
    ]

    let useCityData = [
        {value: '50000,30000', name: 'Dallas'},
        {value: '50000,30000', name: 'Philadelphia'},
        {value: '50000,30000', name: 'Socal'}
    ]

    /**
	 * @type {boolean}
	 */
    let checked = false

    // @ts-ignore
    const clickCheck = () => {
        if (document.getElementById("extra").style.opacity == "0") {
            document.getElementById("extra").style.opacity = "1"
        }
        else {
            document.getElementById("extra").style.opacity = "0"
        }
    }

    const submitForm = () => {
        let uri = `http://localhost:5000/${sqft}/${acrage}/${parcelVal}/${description}/${city}`
    }

</script>

<main id="theMain">
    <div class="div1">
        <Label for='large-input' class='block mb-2'>How many square feet is the property?</Label>
        <Input id="large-input" size="lg" placeholder="square feet" />
    </div>
    <div class="div1">
        <Label for='large-input' class='block mb-2'>How many acres is the property?</Label>
        <Input id="large-input" size="lg" placeholder="acres" />
    </div>
    <div class="div1">
        <Label>Select what type of zone the property is
            <Select class="mt-2" items={useDescCodes} bind:value={descSelected} />
        </Label>
    </div>
    <div class="div1">
        <Label>Select the city the property is in
            <Select class="mt-2" items={useCityData} bind:value={citySelected} />
        </Label>
    </div>
    <div class="div1">
    <Checkbox on:click={() => clickCheck()}>
        Click here if you don't know parcel or median income information
    </Checkbox>
    </div>

    <div id="extra">
        <div class="div1">
            <Label for='large-input' class='block mb-2'>What is the parcel value of the property?</Label>
            <Input id="large-input" size="lg" placeholder="Parcel Value" />
        </div>
        <div class = "div1">
            <Label for='large-input' class='block mb-2'>What is the mean family income of the area?</Label>
            <Input id="large-input" size="lg" placeholder="Mean Family Income" />
        </div>
    </div>

    <div>
        <Button color="dark" on:click = {() => submitForm}>Check Value</Button>
    </div>

</main>

<style>
    #theMain {
        transition: 1s;
    }

    .div1 {
        transition: 1s;
        margin: 1rem;
    }
</style>