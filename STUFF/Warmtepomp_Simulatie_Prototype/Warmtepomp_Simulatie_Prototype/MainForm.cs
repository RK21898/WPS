using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Warmtepomp_Simulatie_Prototype
{
    public partial class MainForm : Form
    {
        Formula f = new Formula(); // usage of formulas needed for the simulation

        public MainForm()
        {
            InitializeComponent();
        }
    }
}
