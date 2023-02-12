<script>
    import { onMount } from 'svelte';
    import { CardPlaceholder, Spinner } from 'flowbite-svelte';
    import { houses, selectedHouse, tempHouse } from './storage';
	import Saos from "saos";
    /**
	 * @type {any}
	 */
     export let caller;

    /**
     * @type {boolean}
    */
   let ready = false

   const change = (/** @type {string} */ val) => {value = val};

    /**
     * @type {string}
     */
     let value;

    const fetchValue = async (/** @type {number} */ sqft, /** @type {number} */ acrage, /** @type {number} */ parcelVal, /** @type {string} */ description, /** @type {string} */ city) => {
    	const url = `http://localhost:5000/${sqft}/${acrage}/-1/${description}/${city}`;
    	const res = await fetch(url).then(async (data) => {
            return await data.json()
        }).catch((e) => {
            console.log(e)
        });
        console.log(res['value'])
        return (res['value'])
	};

    
    onMount(async () => {
        let currentHouse = caller == 'temp' ? $tempHouse : $houses[$selectedHouse] ;
        let val = await fetchValue(currentHouse.sqft, currentHouse.acres, currentHouse.parcelValue,
                                    currentHouse.description, currentHouse.city);
        change(val);
        ready = true;
    });

</script>

<main>
    {#if !ready}
    <div>
        <Spinner size={'20'} />
    </div>
    {:else}
        <Saos top={100} once={true} animation={"fade-in 2s cubic-bezier(0.390, 0.575, 0.565, 1.000) both"}>
            <div id="valueText">The value is ${Number(value).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</div>
        </Saos>
    {/if}
</main>

<style>
    #valueText {
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		font-size: 5rem;
		font-weight: 300;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
    }

	@keyframes -global-fade-in {
		0% {
			opacity: 0;
		}
		100% {
			opacity: 1;
		}
	}
</style>