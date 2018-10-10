using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Warmtepomp_Simulatie_Prototype
{
    public class Formula
    {
        RoomTypeInformation rti;

        /// <summary>
        /// Convert kiloWatthour to joules
        /// </summary>
        /// <param name="kWh"></param>
        /// <returns>the equivalent of x kWh as y joules</returns>
        public decimal WattToJoules(decimal watt)
        => watt * 1000;

        /// <summary>
        /// Calculate the power requirement for a room using
        /// length * width * height * specific power per room
        /// </summary>
        /// <returns>power in watts</returns>
        public decimal PowerRequirementForRoom(decimal length, decimal width, decimal height, string isolationquality)
        {
            decimal capacity = length * width * height;

            int watt;
            rti.RoomTypeInfo.TryGetValue(isolationquality, out watt); //fetch from watt per roomtype table

            return capacity * watt; 
        }

        /// <summary>
        /// Calculate the COP coefficient of the heat pump
        /// power output is the power from the source
        /// added power is power generated from the compressor in the pump
        /// </summary>
        /// <param name="powerOutput"></param>
        /// <param name="addedPower"></param>
        /// <returns>COP coefficient</returns>
        public decimal COP(decimal powerOutput, decimal addedPower)
        => powerOutput / addedPower;

        /// <summary>
        /// Calculates the volume flow rate
        /// Use for both Intake and Output sides in heat pump.
        /// power in Watts
        /// Density in kg/m^3
        /// specific heat in Joule/kg.K
        /// Delta T in Kelvin
        /// </summary>
        /// <param name="power"></param>
        /// <param name="density"></param>
        /// <param name="specific_heat"></param>
        /// <param name="deltaT"></param>
        /// <returns>volume flow rate in m^3/s</returns>
        public decimal WaterFlow(decimal power, decimal density, decimal specific_heat, decimal deltaT)
        => power / (density * specific_heat * deltaT);

        /// <summary>
        /// Seasonal Performance Factor
        /// Qw = Warmth delivered to building by heat pump in MWh
        /// Qk = Cold delivered to building by heat pump in MWh
        /// E = Electricity used by the pump system in MWh
        /// G = Electric equivalent of natural gas used by the pump system in MWh 
        /// </summary>
        /// <param name="Qw"></param>
        /// <param name="Qk"></param>
        /// <param name="E"></param>
        /// <param name="G"></param>
        /// <returns>Seasonal Performance Factor</returns>
        public decimal SPF(decimal Qw, decimal Qk, decimal E, decimal G)
        => (Qw + Qk) / (E + G);
        
        /// <summary>
        /// Calculate the power needed to heat up a substance, like air
        /// m = mass of substance
        /// c = specific heat
        /// DeltaT = temp difference (wanted Temp - current Temp)
        /// </summary>
        /// <param name="m"></param>
        /// <param name="c"></param>
        /// <param name="DeltaT"></param>
        /// <returns>The amount of power required to heat up substance</returns>
        public decimal PowerRequirementToHeatUpSubstance(decimal m, decimal c, decimal DeltaT)
        => (m * c * DeltaT) / 3600000;

        /// <summary>
        /// Calculate the time needed to heat up a substance, like air
        /// power = the output of the device used to heat up substance in kW
        /// requirement = the power needed to heat up substance in kWh
        /// </summary>
        /// <param name="power"></param>
        /// <param name="requirement"></param>
        /// <returns>time requirement in hours * 3600 (so it will be seconds)</returns>
        public decimal TimeRequirementToHeatUpSubstance(decimal power, decimal requirement)
        => (requirement / power) * 3600;
    }
}
